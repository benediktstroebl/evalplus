
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
    
    solar_system = {
        "Mercury": 57909050, 
        "Venus": 108209475, 
        "Earth": 149600000, 
        "Mars": 227943824, 
        "Jupiter": 778330000, 
        "Saturn": 1426714000, 
        "Uranus": 2870993000, 
        "Neptune": 4498252000
    }
    # check if planet1 and planet2 are valid
    if planet1 not in solar_system or planet2 not in solar_system:
        return ()
    
    planets = list(solar_system.keys())
    if planets.index(planet1) < planets.index(planet2):
        return planets[planets.index(planet1) + 1 : planets.index(planet2)]
    else:
        return planets[planets.index(planet2) + 1 : planets.index(planet1)]
