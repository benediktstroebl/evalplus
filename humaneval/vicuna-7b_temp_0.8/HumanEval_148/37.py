
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
    # check for correct planet names
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        return (planet2, planet1)
    elif planet1 == "Saturn" or planet2 == "Saturn":
        return (planet2, planet1)
    elif planet1 == "Uranus" or planet2 == "Uranus":
        return (planet2, planet1)
    elif planet1 == "Neptune" or planet2 == "Neptune":
        return (planet2, planet1)
    elif planet1 == "Venus" and planet2 == "Earth":
        return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Venus" and planet2 == "Mercury":
        return ("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Jupiter":
        return ("Jupiter", "Saturn", "Uranus", "Neptune", "Venus", "Earth", "Mars")
    elif planet1 == "Mars" and planet2 == "Saturn":
        return ("Saturn", "Uranus", "Neptune", "Venus", "Earth", "Jupiter", "Mars")
    elif planet1 == "Mars" and planet2 == "Uranus":
        return ("Uranus", "Neptune", "Venus", "Earth", "Jupiter", "Saturn", "Mars")
    elif planet1 == "Mars" and planet2 == "Neptune":
        return ("Neptune", "Venus", "Earth", "Jupiter", "Saturn", "Uranus", "Mars")
    elif planet1 == "Earth" and planet2 == "Mercury":
        return ("Mercury", "Venus", "Jupiter", "Saturn", "Uranus", "Neptune")
    
