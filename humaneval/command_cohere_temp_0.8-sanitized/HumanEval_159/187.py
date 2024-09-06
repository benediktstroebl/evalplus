def eat(n, need, rem):
    gt, lt = divmod(need, n)
    eaten = n * gt + min(lt, rem)
    return [eaten, max(0, rem - eaten)]