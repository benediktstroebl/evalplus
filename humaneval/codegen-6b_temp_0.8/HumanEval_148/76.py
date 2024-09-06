
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
    planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    nearby = []
    for planet in planets:
        if planet != planet1 and planet != planet2:
            continue
        if planet == planet1:
            if planet2 == "Neptune":
                nearby.append("Jupiter")
                nearby.append("Saturn")
            elif planet2 == "Mars":
                nearby.append("Venus")
                nearby.append("Earth")
            elif planet2 == "Jupiter":
                nearby.append("Uranus")
                nearby.append("Neptune")
            elif planet2 == "Saturn":
                nearby.append("Uranus")
        elif planet == planet2:
            if planet1 == "Neptune":
                nearby.append("Jupiter")
                nearby.append("Saturn")
            elif planet1 == "Mars":
                nearby.append("Venus")
                nearby.append("Earth")
            elif planet1 == "Jupiter":
                nearby.append("Uranus")
                nearby.append("Neptune")
            elif planet1 == "Saturn":
                nearby.append("Uranus")
    
    if planet1 not in planets or planet2 not in planets:
        return nearby
    nearby.sort(key=lambda name: (-abs(planets.index(planet1) - planets.index(name)), name))
    return tuple(nearby)
