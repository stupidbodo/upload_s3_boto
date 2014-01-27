import sys
import boto
import boto.s3
from getpass import getpass
from boto.s3.key import Key


class UploadS3Boto(object):

    def __init__(self, aws_access_key, aws_secret_key, bucket_name, file_name, file_location):
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.file_location = file_location

    def upload_file(self):
        bucket = self._create_get_bucket()
        k = Key(bucket)
        k.key = self.file_name
        k.set_contents_from_filename(file_location)
        print "File Uploaded"

    def _create_get_bucket(self):
        conn = self._conn_s3()
        return conn.create_bucket(self.bucket_name)

    def _conn_s3(self):
        return boto.connect_s3(self.aws_access_key, self.aws_secret_key)

# get information
aws_access_key = raw_input("Please enter AWS Access Key: ")
aws_secret_key = getpass("Please enter AWS Secret Key: ")
bucket_name = raw_input("Please enter bucket name(will be created if not exist): ")
file_name = raw_input("Please enter name of file to be use on S3: ")
file_location = raw_input("Please enter location of file to be uploaded: ")

# setup class
uploads3 = UploadS3Boto(aws_access_key, aws_secret_key, bucket_name, file_name, file_location)

# upload file
uploads3.upload_file()
