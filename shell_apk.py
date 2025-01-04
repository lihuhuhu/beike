def header_authorization(self, community_id: str, page: str):
    """ 请求头中的验证参数 """
    source_str = f'打码cacity_id={community_id}condition=containerType=0limit_count=10limit_offset={page}'
    sha1 = '20180111_android:' + hashlib.sha1(source_str.encode()).hexdigest()
    return base64.b64encode(sha1.encode()).decode()