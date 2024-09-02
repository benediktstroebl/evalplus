
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    #pass
    name_to_dic = {'Mercury':pyorbit.Mercury(0, 0), 'Venus':pyorbit.Venus(0, 0), 'Mars':pyorbit.Mars(0, 0), 'Jupiter':pyorbit.Jupiter(0, 0), 'Saturn':pyorbit.Saturn(0, 0), 'Uranus':pyorbit.Uranus(0, 0), 'Neptune':pyorbit.Neptune(0, 0)}
    near_1 = pyorbit.Sun(pyorbit.AU).distance(name_to_dic[planet1])
    near_2 = pyorbit.Sun(pyorbit.AU).distance(name_to_dic[planet2])
    near_list = []
    for i in name_to_dic:
        if pyorbit.Sun(pyorbit.AU).distance(name_to_dic[i]) > near_2 and pyorbit.Sun(pyorbit.AU).distance(name_to_dic[i]) < near_1:
            near_list.append(i)
    near_list.sort()
    return tuple(near_list)



