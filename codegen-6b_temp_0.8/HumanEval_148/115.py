
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
    if planet1.lower() not in planets or planet2.lower() not in planets:
        return
    planet1, planet2 = planets[planet1.lower()], planets[planet2.lower()]
    try:
        distances = {planet:distance(planet, sun) for planet in planets}
    except:
        return
    return tuple(sorted(planet for planet in planets if distance(planet, sun) > distances[planet1] and distance(planet, sun) < distances[planet2]))
    
