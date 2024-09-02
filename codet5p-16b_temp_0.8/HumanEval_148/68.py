
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

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    for p in planets:
        if p == planet1 or p == planet2:
            pass
        else:
            return None
    
    planet1_ind = planets.index(planet1)
    planet2_ind = planets.index(planet2)
    
    if planet2_ind > planet1_ind:
        return tuple(planets[planet1_ind+1:planet2_ind])
    elif planet2_ind < planet1_ind:
        return tuple(planets[planet1_ind+1:planet2_ind+1][::-1])
    else:
        return tuple()
    
