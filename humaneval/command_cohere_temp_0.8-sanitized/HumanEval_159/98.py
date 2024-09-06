def eat(n, need, rem):
    ate = n
    if need > rem:
        print("Oh no! Go hungry!")
    elif need <= rem:
        ate += need
        print("Delicious meal, rabbit is not hungry now...")
    return [ate, rem]