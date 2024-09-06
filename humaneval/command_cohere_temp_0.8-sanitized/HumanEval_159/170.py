def eat(n, need, rem):
    ate = min(n + min(need, rem), rem)
    full = n + ate
    return [full, rem - ate]