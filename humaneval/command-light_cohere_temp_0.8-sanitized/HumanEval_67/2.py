def fruit_distribution(total_fruits,fruits_type):
    if(fruits_type == 'apples'):
        return total_fruits // 2
    elif(fruits_type == 'oranges'):
        return total_fruits // 3
    elif(fruits_type == 'mangos'):
        return total_fruits // 2
    else:
        return "Invalid fruits type"