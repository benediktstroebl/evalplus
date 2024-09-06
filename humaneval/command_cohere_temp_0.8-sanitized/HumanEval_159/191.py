def eat(n, need, rem):
    bunny_eat = n + need
    leftover = rem - bunny_eat
    return [bunny_eat, leftover]