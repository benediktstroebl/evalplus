def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]