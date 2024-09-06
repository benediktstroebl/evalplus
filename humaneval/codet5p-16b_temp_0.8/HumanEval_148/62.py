
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
    planet_tuples = [(p, planets.index(p)) for p in planets]
    planet_dict = dict(planet_tuples)
    planet1_idx = planet_dict[planet1]
    planet2_idx = planet_dict[planet2]
    if (planet1_idx + 1) > planet2_idx:
        return ()
    else:
        proximity = [i for i in range(planet1_idx + 1, planet2_idx)]
        proximity.reverse()
        return tuple([planets[i] for i in proximity])
    
        
    
