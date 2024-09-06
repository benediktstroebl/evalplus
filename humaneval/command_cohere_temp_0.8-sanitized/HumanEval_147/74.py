def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = arr[i] + arr[j] + arr[j + 1]
            if sum_ % 3 == 0:
                cnt += 1
    return cnt