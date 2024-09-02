
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
    if planet1.lower() == 'earth':
        return tuple(x for x in get_planets() if x < planet2)
    
    elif planet2.lower() == 'earth':
        return tuple(x for x in get_planets() if x > planet1 )
    
    else:
        planets = get_planets()
        result = []
        for planet in planets:
            if planet1.lower() in planet and planet2.lower() in planet:
                if planet.index(planet1.lower()) > planet.index(planet2.lower()):
                    result.append(planet2.lower())
                else:
                    result.append(planet1.lower())
        return tuple(result)
                