def eat(n, need, rem):
    ate = n
    if need > rem:
        print("Oh oh, I'm going to eat everything that I have left...")
        need = rem
    print("I'm hungry, I'm going to eat...")
    for i in range(need):
        print("Bite {}!".format(i+1))
        ate += 1
    print("Yay, I'm full now!")
    return [ate, rem]