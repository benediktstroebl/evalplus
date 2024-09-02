
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if not planet1 or not planet2:
        return ()
    
    if planet1 == "Mercury" and planet2 == "Mercury":
        return planets.copy() # empty tuple
    elif planet1 == "Mercury" and planet2 == "Venus":
        return ("Venus",)
    elif planet1 == "Venus" and planet2 == "Venus":
        return planets.copy() # empty tuple
    elif planet1 == "Venus" and planet2 == "Mercury":
        return ("Mercury",)
    elif planet1 == "Earth" and planet2 == "Earth":
        return planets.copy() # empty tuple
    elif planet1 == "Earth" and planet2 == "Mars":
        return ("Mars",)
    elif planet1 == "Earth" and planet2 == "Jupiter":
        return ("Jupiter",)
    elif planet1 == "Earth" and planet2 == "Saturn":
        return ("Saturn",)
    elif planet1 == "Earth" and planet2 == "Uranus":
        return ("Uranus",)
    elif planet1 == "Earth" and planet2 == "Neptune":
        return ("Neptune",)
    elif planet1 == "Mars" and planet2 == "Mars":
        return planets.copy() # empty tuple
    elif planet1 == "Mars" and planet2 == "Earth":
        return ("Earth",)
    elif planet1 == "Mars" and planet2 == "Jupiter":
        return ("Jupiter",)
    elif planet1 == "Mars" and planet2 == "Saturn":
        return ("Saturn",)
    elif planet1 == "Mars" and planet2 == "Uranus":
        return ("Uranus",)
    elif planet1 == "Mars" and planet2 == "Neptune":
        return ("Neptune",
