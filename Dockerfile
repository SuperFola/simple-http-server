FROM elyase/staticpython
WORKDIR /var/www/
COPY entrypoint.py /usr/bin/
EXPOSE 8080
CMD [ "python", "/usr/bin/entrypoint.py" ]