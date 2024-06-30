import requests

def GetHost():
    cookies = {
    'SID': 'g.a000hwgTIEy1rLNcmbnhx1IB35XlXiNemOJUagc3rgDeiTICKYGh-peiL-ps4wb-RD8U3Spw9QACgYKAaISAQASFQHGX2MiT49b2eTpK-hgV1wQo4zXThoVAUF8yKp9AfAeZrdm9sKg7ZHa95DP0076',
    '__Secure-1PSID': 'g.a000hwgTIEy1rLNcmbnhx1IB35XlXiNemOJUagc3rgDeiTICKYGh1Utd-vKx_Bh3I6wajpdb8QACgYKAUwSAQASFQHGX2MiJd9qF5d9rgHmFX6U9cckdBoVAUF8yKq6lXWvPR-NPut_5LDzz2Go0076',
    '__Secure-3PSID': 'g.a000hwgTIEy1rLNcmbnhx1IB35XlXiNemOJUagc3rgDeiTICKYGhb1Fcm5J_0Be0MUJsCQy9cQACgYKATESAQASFQHGX2MiSbY_dlaRgY5nDbJyh7AYwBoVAUF8yKpcwxLTyHThCGNPZ0j8hg3v0076',
    'LSID': 's.youtube:g.a000hwgTIBQyDLKWhCNHOs5hzSqDAAMwaAblo45F0-dC5enegdVz7N6jG9idM9mQCnx7j6i_2AACgYKAaMSAQASFQHGX2Mi9dpw20B7BxkqIb99i0tj3hoVAUF8yKp_oYFYtIO7-vzA4kiXORxK0076',
    '__Host-1PLSID': 's.youtube:g.a000hwgTIBQyDLKWhCNHOs5hzSqDAAMwaAblo45F0-dC5enegdVzknBHPXVwejxkfe72vNZWVgACgYKAd8SAQASFQHGX2Mier3H-HUixaRxqS66YUKPBBoVAUF8yKqlrjblRJoLaqpboPengdb60076',
    '__Host-3PLSID': 's.youtube:g.a000hwgTIBQyDLKWhCNHOs5hzSqDAAMwaAblo45F0-dC5enegdVz712tR_LVmHlZjScoKg8oJAACgYKAacSAQASFQHGX2MiPnRfewNUFt29gmeMH6TxkRoVAUF8yKqY9OCpZhqQwnmNoGK9H5gd0076',
    'HSID': 'AdjofRZTXAY9QGmsf',
    'SSID': 'AumpMXlVfC7Xd9Vwu',
    'APISID': 'uqsvbAnPIpknXeTQ/AEZGV50qvYv6QQCpA',
    'SAPISID': '-ZHDZlpxyftCQPY5/Awy58l7WzeHoaBGtG',
    '__Secure-1PAPISID': '-ZHDZlpxyftCQPY5/Awy58l7WzeHoaBGtG',
    '__Secure-3PAPISID': '-ZHDZlpxyftCQPY5/Awy58l7WzeHoaBGtG',
    'ACCOUNT_CHOOSER': 'AFx_qI47y3KH70aX-OAQyeVJB77vpmGnBMKLlvndx7m1to3hWlocU1rJyTH2hg4cr6qcSog5Spq9atBRCeCnmjFigHiRKJavEeTvdlTvubPWDqs_4btr3Lp2S2pjZAJL36t7u9qKyhUP4udeoaDWuhGI1osMJa1oWrR5jN07QkEgYCSEJly6f1J18Z3vHH_kP_-g56p9-xGvE8jG6KOLukgrG9WuM3Quy-ogvB4xEZ_6k3lxamNIh2k',
    'LSOLH': '|_SVI_EM7599mwj4UDGAMiP01BRURIZl9xcDhmbXRNdEhfS3drRnBuTUsxZlJ0LWtwU2t3bjU2eEtvNW10VURpOG9WZjdxUnpHS3Qtamg4SQ_:|28522824:5bfe',
    'SIDCC': 'AKEyXzXb7GpP5yzuDQa5yTtH_G7f1KUK8CO28MWZk-ScsakIRkuYEcCXy38j-qnPwOIyod29dg',
    '__Secure-1PSIDCC': 'AKEyXzWCvK-vmstcjEyni5xH836nLW9dPgPoWf1BauxuqFBOjPQVhbp8G7zkDs6vjqZcaeeAWA',
    '__Secure-3PSIDCC': 'AKEyXzUbyA5juXVY7V0yAFjpv0en8fNtHLQ0XpsQNKyEzB7xXfMJepQBm4c0cXBrqYaSXb45BA',
    'AEC': 'AQTF6HySTfF40SOCNwEwO9JKxLU53NVOSaO3F_v8Jgjwmsy4TSRFKtfccXw',
    '1P_JAR': '2024-06-08-10',
    '__Host-GAPS': '1:TgGw5aHC_B2wIAR-otlWDzW_pKmcz5cmEs7a_0QlS9-pkkCY1q5VXVhZwA8TNSjnsjywSKBOG2PsnI9s0rviTN8ByTKf4A:ZkcCOKl_5e5hPwLP',
    'NID': '515=s_QZ_1nChxQgxcE4svzyw4tk94V7Dh1_StjYduFyAoUNTRSjTschTyeQzjPEkMA45k8ptfn3BwytkvbE0oPgelyUBpmReAbaIp1MYtErLu_Kd9GkDqUvyovUYgy3ppnR5AbMIk556gJ46-SlirBeCASrtS6ZsQcc7pA5xlFZcAXbHMLVBj0wHdFPCP9vrucjf5475MEYmmUdZCpAgJvwMqnw_Q4pCF8LtLU8U_AN0T6kXgBqyUwP5UavPrhvNEyE2tc2',
    'OTZ': '7619934_44_44__44_',
}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',    
    'priority': 'u=0, i',
    'referer': 'https://accounts.google.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"126.0.2592.68"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.114", "Microsoft Edge";v="126.0.2592.68"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
}

    params = {
    'continue': 'https://accounts.google.com/b/0/AddMailService',
    'followup': 'https://accounts.google.com/b/0/AddMailService',
    'passive': '1209600',
    'ifkv': 'AS5LTAQ7hDdWxjnKrzfmBdi2ndcU7MRtjNcJ_CpCqpII9DxB7stRslcs5b51SZA0bmLeZQYpWS0HtA',
    'ddm': '0',
    'flowName': 'GlifWebSignIn',
    'flowEntry': 'ServiceLogin',
}

    Host = requests.get('https://accounts.google.com/v3/signin/identifier', params=params, headers=headers, cookies=cookies).cookies["__Host-GAPS"]
    try:
    	os.remove("HostGoogle.txt")
    except:
    	pass
    with open("HostGoogle.txt", "a") as f:
    	f.write(Host +'\n')
    
    
def Check(email):
    try:
        try:
            with open("HostGoogle.txt", "r") as f:
                for line in f:
                    Host = line.strip()
        except:
            GetHost()
            with open("tlcok.txt", "r") as f:
                for line in f:
                    Host = line.strip()
        if "@" in email:
            name = str(email.split('@')[0])
        else:
            name = email       
        cookies = {
            '__Host-GAPS': Host,
        }

        headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    
    'origin': 'https://accounts.google.com',
    'priority': 'u=1, i',
    'referer': 'https://accounts.google.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"126.0.2592.68"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.114", "Microsoft Edge";v="126.0.2592.68"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': '["S-2130084989:1719500029527702",null,null,"AS5LTAQ7hDdWxjnKrzfmBdi2ndcU7MRtjNcJ_CpCqpII9DxB7stRslcs5b51SZA0bmLeZQYpWS0HtA"]',
    'x-same-domain': '1',
}

        params = {
            'rpcids': 'V1UmUe',
            'source-path': '/v3/signin/identifier',
            'f.sid': '-6546798125074414583',
            'bl': 'boq_identityfrontendauthuiserver_20240609.08_p0',
            'hl': 'ar',
            '_reqid': '264441',
            'rt': 'c',
        }

        data = 'f.req=%5B%5B%5B%22V1UmUe%22%2C%22%5Bnull%2C%5C%22'+name+'%40gmail.com%5C%22%2C1%2Cnull%2Cnull%2C1%2C1%2Cnull%2Cnull%2C%5C%22S-2130084989%3A1719500029527702%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%5D%2Cnull%2C%5C%22%5C%22%2C%5C%22YE%5C%22%2C%5Bnull%2Cnull%2C%5C%22S-2130084989%3A1719500029527702%5C%22%2C%5C%22ServiceLogin%5C%22%2C%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%2Cnull%2C%5B%5B%5C%22continue%5C%22%2C%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%5D%2C%5B%5C%22followup%5C%22%2C%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%5D%2C%5B%5C%22passive%5C%22%2C%5C%221209600%5C%22%5D%2C%5B%5C%22ifkv%5C%22%2C%5C%22AS5LTAQ7hDdWxjnKrzfmBdi2ndcU7MRtjNcJ_CpCqpII9DxB7stRslcs5b51SZA0bmLeZQYpWS0HtA%5C%22%5D%2C%5B%5C%22ddm%5C%22%2C%5C%220%5C%22%5D%2C%5B%5C%22flowName%5C%22%2C%5C%22GlifWebSignIn%5C%22%5D%2C%5B%5C%22flowEntry%5C%22%2C%5C%22ServiceLogin%5C%22%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B%5C%22%5C%22%2C%5C%22%5C%22%2C0%5D%2Cnull%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C1%5D%2Cnull%2C7%2Cnull%2C%5B%5B%5C%22identity-signin-identifier%5C%22%2C%5C%22!MjGlMWnNAAbTqBB886hCPLiprKPga3Y7ADQBEArZ1GrR5EQJUy7ogzKkaEFlbY9qyeuvJPzTjx11g1Pxvoj7eqBaAfy95Bywtl2THJacAgAAACNSAAAAE2gBB34AQ1oUvRKIc4CoPydJtDcLQN9rpIQTEG7J9swXekpHmBrSoKUqowP64D64rW-WbwaGI_cqsJI-uKqYm-sBgkUUfZX9SfmZBQLCd1g_OJLY3GSBxTkXaImS0fIlK06uAC4vvgFU7aNWVp7NejxukfLOVS_3wHb1lHafwLZwQs5ZNm7EVPNHfbBTqgEodkiKAX2O_uYhvfPp1aZtqlSDsNPIfR8EHAzJ5KdyFmIwqmqYY9v4k4FIav5NaBoZpqBasc6NiKEtLEA0O5QacJyd2UqY83ybjYh5JL52G3xluVdtnH8YAb1rPKgZPhB6YVUR3Gmh6MqURyB71yU33X5BTeMJDiLfhY-Y9isfXSzDWeChzuztjZriZRul1BPvi9LHCRqa1kexH74TKPRlEUYXAO1nDAhCHoSKhKXoeqyfPF3VXA_yD3H3GtXZGN63AGJ9P_zF9WBWdgfYl2k5W8G9FNMgXmPLEOjhzu1Sma0FjNqPb9mTnhZMrXZzV1ImncCGoQK_eIRWCwnk3pB4sT1669nj4I19hYWcMUhlIw_QIRia_UcyMhXZq7qFgbalt25iJnZXu7ibmaCiXHYYkL-BFPwHUoXbNtFspTXmXlt6YasGljLWFMDf7WyOoV87NPHQ7STjGGePtthQScfsXbbhPWYZl0TbUNV6FI_vwU1s5qy-a-D6YdQYWgCCjFGSMw5gPbHev2vLu5C6hnvRY9LiDXBG1M4yQbv7xIeIzNa42flwgicIRtVHOZVBj1iyvexem0fS81sGm9zxghy31NAZXdIJJSnMjlslO8YSBXHM_ke9n3s_0_1mmCKgutGJLYuOQJyRMmkuwJezxyfRMnTvt1FLzw6xADCudEP4rDbZC0qJYEHozl3jELcbUbcD4XLGYqP3g4Gv5Y5CvVaqnCwf-x1Bmqvo7wwLh4Szb1mMW9nIfCaslL4f7fGn1vF4q62p00FhZ_bVhNTRr9KbDbywSYj8CimJYWA5pAPKUQdg6ATUkGdWBC0b5rHr-iGo1Gw2o3fHrOg4VKtbkRfU_J5JPw61N1X5s5EGuNZGadpg1_xK-c_z6lIVA1966Pr9UJeWKwi8y4Uj2qgo1-SEcaLvdpjSa8Ip14lB9Sl-cGEgDNjZHJVRkWydILqbd7FLORcnXzI5amlq4S-FlpT4dwB0ldwKI5NcQcxnElXe4Mc0_g7ZwsShRODM5gFyxHmSVHOVs_-AFwj_KcYOQEy8SrTNI7seNRp8YTlg4juzUlKNVvREKoCG9g-m-ShEMgph2ilhL7Z5dAlG1H8U29eJdSq5V0wV14YHneOJukM1_GQW60w-2W3h3jKwW_5jomRiW7rZUnGyC_Rwm7P2QelcEY_QB1SPftCTp7_uQD_s5dNUnOaRk1YvzsGofa2wg4m-biGfKHUIidAj2qTiJbpaddcMwBX7xf3ZrVZqUOQzMqa_5rntbBGxv3pLlS4H27ZZyurIQCLQ6vLAaYnaKPlJapuemSI3_RwQuxsqvVY65rqGD9CYGk6HKGLFkBQsOLsBPs1husfNThZlZOy6vjN-q6Jsyewnlp65jDmDZbLqhTXzmcPhY-ajIzvjKSDqz5NEDUiI9pkbhSQBuou-i8AriNIDU8anRWmoHeJH-u7hZxniEapbKShCenWBxAhP_grllTNiovwGG1ZH-Z0W6NoBEf1xyJ_lnMsPlSOQNa-14MmZEK0E34PJDcpQYr10jmG7PKZizJeXYio0sGIT3AaEaaGHaQW81tFnADCVHVpXN4EglbYvUsBPqFfsxEbH_MhvuA1PdQoNGd9hGKuZgAev%5C%22%5D%5D%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C%5B%5B%5C%22continue%5C%22%2C%5B%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%5D%5D%2C%5B%5C%22followup%5C%22%2C%5B%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%5D%5D%2C%5B%5C%22passive%5C%22%2C%5B%5C%221209600%5C%22%5D%5D%2C%5B%5C%22ifkv%5C%22%2C%5B%5C%22AS5LTAQ7hDdWxjnKrzfmBdi2ndcU7MRtjNcJ_CpCqpII9DxB7stRslcs5b51SZA0bmLeZQYpWS0HtA%5C%22%5D%5D%2C%5B%5C%22ddm%5C%22%2C%5B%5C%220%5C%22%5D%5D%2C%5B%5C%22flowName%5C%22%2C%5B%5C%22GlifWebSignIn%5C%22%5D%5D%2C%5B%5C%22flowEntry%5C%22%2C%5B%5C%22ServiceLogin%5C%22%5D%5D%5D%2C%5C%22https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService%5C%22%5D%2Cnull%2C%5C%22S-2130084989%3A1719500029527702%5C%22%2Cnull%2Cnull%2C%5B%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=ALt4Ve09VpeGevTAFM0V6Tq2gnBh%3A1719500029532&'

        res = requests.post(
            'https://accounts.google.com/v3/signin/_/AccountsSignInUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).text
        if '/v3/signin/rejected' in res or f'{name}@gmail.com' in res:
            print(f"Is_Available  - False -  {name}@gmail.com")
        elif 'gf.uicd' in res:           
            print(f"Is_Available  - True -  {name}@gmail.com")
            
        else:
            GetHost()
            print('Try again later')
        
    except:
        print("TURN VPN")


Check(input("ENTER EMAIL GMAIL :"))