
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
    # check if the input planets are correct
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] \
       or planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    # create a list of planets in between
    planets = []
    for i in range(1, 10):
        distance = (i - 1) * 14959787070000.0
        if distance >= planet1 - 14959787070000.0 and distance <= planet2 + 14959787070000.0:
            planets.append(planet_names[i])
    
    # sort the list by the proximity to the sun
    planets = sorted(planets, key=lambda x: -x)
    
    return planets
