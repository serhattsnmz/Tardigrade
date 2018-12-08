FROM alpine:latest
MAINTAINER Furkan SAYIM <furkan.sayim@yandex.com>

ARG DOMAIN=""
ARG VERBOSE=""
ARG SAVEFILE=""

ENV DOMAIN=${DOMAIN}
ENV VERBOSE=${VERBOSE}
ENV SAVEFILE=${SAVEFILE}

RUN apk update && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN mkdir /tardigrade
ADD requirements.txt /tardigrade
ADD tardigrade.py /tardigrade

WORKDIR /tardigrade

RUN pip3 install -r requirements.txt

CMD python3 tardigrade.py -d ${DOMAIN} -t ./subdomain.txt -v ${VERBOSE} -s ${SAVEFILE}
