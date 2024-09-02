
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
    
    if planet1 == "Mercury":
        # Mercury is the closest planet to the sun
        if planet2 == "Mercury":
            return ("Mercury",)
        elif planet2 > "Mercury":
            return ()
        else:
            return ("Mercury",)
    elif planet1 == "Venus":
        # Venus is the second closest planet to the sun
        if planet2 == "Venus":
            return ("Venus",)
        elif planet2 > "Venus":
            return ()
        else:
            return ("Venus",)
    elif planet1 == "Earth":
        # Earth is the third closest planet to the sun
        if planet2 == "Earth":
            return ("Earth",)
        elif planet2 > "Earth":
            return ()
        else:
            return ("Earth",)
    elif planet1 == "Mars":
        # Mars is the fourth closest planet to the sun
        if planet2 == "Mars":
            return ("Mars",)
        elif planet2 > "Mars":
            return ()
        else:
            return ("Mars",)
    elif planet1 == "Jupiter":
        # Jupiter is the fifth closest planet to the sun
        if planet2 == "Jupiter":
            return ("Jupiter",)
        elif planet2 > "Jupiter":
            return ()
        else:
            return ("Jupiter",)
    elif planet1 == "Saturn":
        # Saturn is the sixth closest planet to the sun
        if planet2 == "Saturn":
            return ("Saturn",)
        elif planet2 > "Saturn":
            return ()
        else:
