
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
    
    if planet1 not in PLANETS or planet2 not in PLANETS:
        return tuple()
    
    orbits = set()
    for planet in PLANETS:
        orbits.add(get_orbit(planet, planet1))
        orbits.add(get_orbit(planet, planet2))
    orbit1 = get_orbit(planet1, planet2)
    orbit2 = get_orbit(planet2, planet1)
    
    if orbit1 < orbit2:
        return tuple(sorted(orbits, key=lambda x:get_orbit(planet1, x)))
    elif orbit1 > orbit2:
        return tuple(sorted(orbits, key=lambda x:get_orbit(planet2, x)))
    else:
        return tuple(sorted(orbits, key=lambda x:get_orbit(planet2, x)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
