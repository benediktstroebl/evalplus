
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
    planets = (("Mercury", 57909227), ("Venus", 108208003), ("Earth", 149600000),
                ("Mars", 227943829), ("Jupiter", 778363300), ("Saturn", 1429461540),
                ("Uranus", 2870995500), ("Neptune", 4498398600))
    try:
        planet1 = int(planets[planets.index(planet1)][1])
    except ValueError:
        return ()
    try:
        planet2 = int(planets[planets.index(planet2)][1])
    except ValueError:
        return ()
    planets = [x for x in planets if planet1 <= int(x[1]) <= planet2]
    planets.sort(key = lambda x: x[1])
    return (x[0] for x in planets)
    
    
    
    
