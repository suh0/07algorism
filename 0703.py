def bm_match(txt: str, pat: str) -> int:
    """보이어-무어 알고리즘으로 문자열 검색"""
    skip = [len(pat)] * 256

    for i in range(len(pat) - 1):
        skip[ord(pat[i])] = len(pat) - i - 1

    pt = len(pat) - 1
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += max(skip[ord(txt[pt])], len(pat) - pp)
    return -1

if __name__ == '__main__':
    s1 = input("텍스트 입력: ")
    s2 = input("패턴 입력: ")

    idx = bm_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx + 1}번째 문자가 일치합니다.")
