
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

    # 이 문제는 단순히 n에 대한 정수 배열을 생성한 뒤, 각 요소를 i*i-i+1 으로 초기화한다.
    # 그 다음 이중 반복문을 통해 각 i 값을 가지고 j 값을 증가시키면서 이 조건이 만족되는지 확인하여 카운트한다.
    # 만약 이 조건이 모두 만족되면 카운트를 증가시키고 반복문이 종료되면 전체 카운트를 반환한다.

    arr = []

    for i in range(n):
        arr.append(i * i - i + 1)

    count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] + arr[j
