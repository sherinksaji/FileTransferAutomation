import paramiko

def upload_file_sftp(local_file, remote_file, host, port, username, password):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload a file
        sftp.put(local_file, remote_file)
        print(f"File {local_file} uploaded to {remote_file}")

    except paramiko.SSHException as e:
        print(f"Failed to upload due to SSH error: {e}")
    finally:
        sftp.close()
        transport.close()

# Usage
upload_file_sftp('test.txt', 'test.txt', 'your_host', 22, 'sherin', 'filetransfer')
