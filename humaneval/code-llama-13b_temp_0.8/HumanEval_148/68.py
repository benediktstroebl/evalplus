
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
    if planet1 not in planets or planet2 not in planets:
        return ()
    planets_ = planets.copy()
    planets_.pop(planet1)
    planets_.pop(planet2)
    planets_ = list(planets_.values())
    planets_ = [i for i in planets_ if planet1 in i and planet2 in i]
    planets_ = sorted(planets_, key=lambda x: x.index(planet1))
    if len(planets_) == 0:
        return ()
    return tuple(sum([i[1:i.index(planet2)], i[:i.index(planet1) + 1]] for i in planets_[1:], planets_[0][:planets_[0].index(planet1) + 1]))
    
    
    
