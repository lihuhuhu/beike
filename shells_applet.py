def handle_authorization(params: dict) -> str:
    """authorization 算法"""
    sort_params = sorted(params.items())
    fix_cypher = '6e8566e348447383e16不方便展示'  # 固定密钥
    source_str = ''

    for key, value in sort_params:
        source_str += f"{key}={value}"

    source_str += fix_cypher
    md5 = hashlib.md5(source_str.encode('utf-8')).hexdigest()

    # base64 编码
    source_str = "打码:" + md5
    result = base64.b64encode(source_str.encode()).decode()
    return result