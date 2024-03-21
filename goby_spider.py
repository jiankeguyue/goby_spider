#! usr/bin/env python
#  writer yueji0j1anke


import argparse
import requests
import colorama
import config
import os
import pandas as pd
from colorama import init, Fore, Style
init()

def title():
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + "  _____          _ _    _       _   ")
    print(" |_   _|        | (_)  | |     | |  ")
    print("   | | _ __  ___| |_  | | ___ | |_ ")
    print("   | || '_ \/ __| | | | |/ _ \| __|")
    print("  _| || | | \__ \ | | | | (_) | |_ ")
    print("  \___/_| |_|___/_| |_|_|\___/ \__|")
    print("goby_spider         writer: yueji0j1anke")
    print(Style.RESET_ALL)



def clear_screen():
    # Clear screen for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')


def getdata(filepath):
    # 初始化信息
    vuln_name_list = []
    vuln_description_list = []
    product_name_list = []
    fofa_query_list = []
    cve_id_list = []
    vuln_type_list = []

    url = 'https://gobysec.net/api/poc-push-list'
    headers = {
        'Cookie': config.cookie,
        'Referer': 'https://gobysec.net/updates',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/10',
    }
    try:
       response = requests.get(url=url,headers=headers)
       json_data = response.json()
    except Exception as e:
        print(colorama.Fore.RED + '[error] 请求时发生故障: {}'.format(e))

    vulnss_data = json_data['data']
    print(colorama.Fore.GREEN + '[info] 正在爬取中........')
    for vulns_data in vulnss_data:
        push_data = vulns_data['push_data']
        for vuln_data in push_data:
            list_append(vuln_name_list,vuln_description_list,product_name_list,fofa_query_list,cve_id_list,vuln_type_list,vuln_data)
    print(colorama.Fore.GREEN + '[info] 爬取完毕，共完成爬取 {} 条'.format(len(vuln_name_list)))
    data_save(vuln_name_list,vuln_description_list,product_name_list,fofa_query_list,cve_id_list,vuln_type_list,filepath)



def list_append(vuln_name_list,vuln_description_list,product_name_list,fofa_query_list,cve_id_list,vuln_type_list,vuln_data):
    vuln_name_list.append(vuln_data.get('name',''))
    vuln_description_list.append(vuln_data.get('description', ''))
    product_name_list.append(vuln_data.get('product',''))
    fofa_query_list.append(vuln_data.get('fofa_query',''))
    cve_id = vuln_data.get('cve_id','')
    if cve_id != '':
        cve_id_list.append(vuln_data.get('cve_id',''))
    else:
        cve_id_list.append("无编号")
    vuln_type_list.append(vuln_data.get('tags',''))



def data_save(vuln_name_list,vuln_description_list,product_name_list,fofa_query_list,cve_id_list,vuln_type_list,file_path):
    df = pd.DataFrame(
        {
            '漏洞名': vuln_name_list,
            '漏洞描述': vuln_description_list,
            '组件名': product_name_list,
            'fofa语法': fofa_query_list,
            'CVE编号': cve_id_list,
            '漏洞类型': vuln_type_list,
        }
    )
    if os.path.exists(file_path + '.csv'):
        header = False
    else:
        header = True
    if not os.path.exists("data"):
        os.mkdir("data")
    df.to_csv('data/' + file_path, mode="a+", header=header, index=False, encoding='utf_8_sig')
    print(colorama.Fore.GREEN + "[success] 文件已生成至data目录")



if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser("spider made by yueji0j1anke")

    parser.add_argument(
        '-o', '--file', required=True,
        metavar='', type=str, default='output.csv',
        help='Please input output file path. eg: output.csv'
    )

    args = parser.parse_args()
    getdata(args.file)