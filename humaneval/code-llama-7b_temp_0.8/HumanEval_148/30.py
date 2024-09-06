
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
    planet_names = {
        'mercury' : 1,
        'venus' : 2,
        'earth' : 3,
        'mars' : 4,
        'jupiter' : 5,
        'saturn' : 6,
        'uranus' : 7,
        'neptune' : 8
    }
    planet1_num = planet_names[planet1.lower()]
    planet2_num = planet_names[planet2.lower()]
    
    return_list = []
    for i in planet_names:
        if planet_names[i] < planet1_num and planet_names[i] > planet2_num:
            return_list.append(i)
    
    return return_list

