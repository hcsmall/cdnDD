def get_real_ip(domain):
    # 实现获取真实IP的函数（与上面给出的脚本相同）

if __name__ == "__main__":
    filename = "websites.txt"

    with open(filename, "r") as file:
        websites = file.read().splitlines()

    for website in websites:
        real_ip = get_real_ip(website)
        print(f"网站 {website} 的真实IP地址是: {real_ip}")
