
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
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet1 == "Mercury" or planet2 == "Mercury":
        # Mercury is closest to the Sun
        return (("Mercury",), ("Venus",))
    if planet1 == "Venus" or planet2 == "Venus":
        # Venus is second closest to the Sun
        return (("Venus",), ("Earth",))
    if planet1 == "Earth" or planet2 == "Earth":
        # Earth is third closest to the Sun
        return (("Earth",), ("Mars",))
    if planet1 == "Mars" or planet2 == "Mars":
        # Mars is fourth closest to the Sun
        return (("Mars",), ("Jupiter",))
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        # Jupiter is fifth closest to the Sun
        return (("Jupiter",), ("Saturn",))
    if planet1 == "Saturn" or planet2 == "Saturn":
        # Saturn is sixth closest to the Sun
        return (("Saturn",), ("Uranus",))
    if planet1 == "Uranus" or planet2 == "Uranus":
        # Uranus is seventh closest to the Sun
        return (("Uranus",), ("Neptune",))
    if planet1 == "Neptune" or planet2 == "Neptune":
        # Neptune is eighth closest to the Sun
        return (("Neptune",))
    
