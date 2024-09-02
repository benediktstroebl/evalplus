
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

    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    distance_from_sun = []
    for planet in planets:
        if planet == planet1 or planet == planet2:
            continue
        x1, y1 = bf(planet1, planet)
        x2, y2 = bf(planet2, planet)
        distance = abs(x1 - x2) + abs(y1 - y2)
        distance_from_sun.append((planet, distance))
    
    return sorted(distance_from_sun, key=lambda x: x[1])
    
