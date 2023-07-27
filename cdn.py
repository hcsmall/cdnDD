# -*- coding: utf-8 -*-

import socket

def is_cdn_domain(domain):
    cdn_domains = [
        '.cdn.cloudflare.net',
        '.edgecastcdn.net',
        '.akamaihd.net',
        '.maxcdn.com',
        '.cloudfront.net',
        '.cachefly.net',
        # 根据需要添加更多 CDN 域名
    ]

    try:
        # 获取与域名相关联的 IP 地址列表
        ip_addresses = socket.gethostbyname_ex(domain)[2]

        # 检查是否有任何 IP 地址与 CDN 域名相关
        for ip_address in ip_addresses:
            aliases = socket.gethostbyaddr(ip_address)[1]
            for alias in aliases:
                for cdn_domain in cdn_domains:
                    if cdn_domain in alias:
                        return True

        return False

    except socket.gaierror:
        return False

if __name__ == "__main__":
    file_path = input("请输入包含域名列表的文本文件路径: ")

    try:
        with open(file_path, 'r') as file:
            domains = file.read().splitlines()

        for domain in domains:
            if is_cdn_domain(domain):
                print(f"{domain} 使用了 CDN.")
            else:
                print(f"{domain} 没有使用 CDN.")

    except FileNotFoundError:
        print("文件未找到，请检查文件路径并重试。")
