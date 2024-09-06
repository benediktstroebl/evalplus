
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # n を 1 進数に変換
    n = int(n)

    # a の配列を初期化
    a = [n]

    # 配列に i を追加する
    for i in range(2, n):
        a.append(i * i - i + 1)

    # 検索する対象となる三角形の検索を開始
    seen = set()  # 対象となる三角形が見つかった場合に、它を保存するリスト
    count = 0  # 対象となる三角形が見つかった場合に、その数が1桁以上である場合に、この値を increment する

    # 検索を行う
    for i in range(1, n):
        # 該当する三角形が見つかった場合
        if i not in seen:
            # 対象となる三角形の数が1桁以上である場合
            if (i - 1, i, i + 1) in seen:
                count += 1
            # 対象となる三角形の数が1桁未満である場合
            else:
                seen.add((i - 1, i, i + 1))
                count = 1

    return count