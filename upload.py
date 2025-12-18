import json
from datetime import datetime
import paramiko
import os


def copy_to_server(local_file_path, remote_file_path, hostname, username):
    # 使用paramiko通过SFTP连接并传输文件
    try:
        # 创建SSH客户端
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接到远程服务器
        ssh.connect(hostname=hostname, username=username)

        # 打开SFTP会话
        sftp = ssh.open_sftp()

        # 将文件上传到远程服务器
        sftp.put(local_file_path, remote_file_path)

        # 关闭SFTP会话
        sftp.close()
        ssh.close()

        print(f"Successful")

    except Exception as e:
        print(f"Failed to copy file: {str(e)}")


if __name__ == '__main__':
    # 复制HTML文件到远程服务器
    copy_to_server(
        local_file_path='/Users/ryan/Ryan/4_codes/yzwbio.github.io/index.html',
        remote_file_path='/www/web/malab_cloudfood_me/public_html/~wyz/index.html',
        hostname='123.57.240.48',
        username='wangyizheng'  # 替换为你登录服务器时使用的用户名
    )
    # copy_to_server(
    #     local_file_path='/Users/wangyizheng/Ryan/4_codes/homepage/index.html',
    #     remote_file_path='/www/web/malab_cloudfood_me/public_html/~wyz/index.html',
    #     hostname='123.57.240.48',
    #     username='wangyizheng'  # 替换为你登录服务器时使用的用户名
    # )