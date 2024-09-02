
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
    # Hint: you can use the math.pi constant
    p1 = planets.index(planet1.capitalize())
    p2 = planets.index(planet2.capitalize())
    
    if p1 < p2:
        start = p1
        end = p2+1
    else:
        start = p2
        end = p1+1
    
    ls = list()
    for i in planets[start:end]:
        if p1 < p2:
            pair = (planets[p1], planets[p2])
        else:
            pair = (planets[p2], planets[p1])
        if pair[0] < pair[1]:
            ls.append(pair[0])
        else:
            ls.append(pair[1])
    
    return tuple(ls)

