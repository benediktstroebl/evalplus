
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
    #planets = {'Mercury':1, 'Venus':2, 'Earth':3, 'Mars':4, 'Jupiter':5,
    #            'Saturn':6, 'Uranus':7, 'Neptune':8}
    planets = {'Mercury':1, 'Venus':2, 'Earth':3, 'Mars':4, 'Jupiter':5,
               'Saturn':6, 'Uranus':7, 'Neptune':8}

    if not planet1 in planets or not planet2 in planets:
        return tuple()
    a = planets[planet1]
    b = planets[planet2]
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        if i == a:
            result = [planet1]
        elif i == b:
            result += [planet2]
        else:
            result += [i]
    return tuple(result)
