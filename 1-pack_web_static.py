#!/usr/bin/python3

from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    """
    this script that generates the archive
    of the contents of web_static folder
    """

    compressedFile = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(compressedFile))

        return "versions/web_static_{}.tgz".format(compressedFile)

    except Exception as e:
        return None
