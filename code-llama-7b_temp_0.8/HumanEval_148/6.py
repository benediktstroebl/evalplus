
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



    # True: planet1 < planet2
    # False: planet1 > planet2
    # True: -2 > 2
    # False: -2 < 2
    def compare_planets(planet1, planet2):
        list_planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        if planet1 not in list_planets:
            return False
        if planet2 not in list_planets:
            return False
        return list_planets.index(planet1) - list_planets.index(planet2)

    # return a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2
    # 1. 
    # 2. 
    # 3. 
    # 4. 
    # 5. 
    # 6. 
    # 7. 
    # 8. 
    # 9. 
    # 10. 
    # 11. 
    # 12. 
    # 13. 
    # 14. 
    # 15. 
    # 16. 
    # 17. 
    # 18. 
    # 19. 
    # 20. 
    # 21. 
    # 22. 
    # 23. 
    # 24. 
    # 25. 
    # 26. 
    # 27. 
    # 28. 
    # 29. 
    # 30. 
    # 31. 
    # 32. 
    # 33. 
    # 34. 
    # 35. 
    # 36. 
    # 37. 
    # 38. 
    # 39. 
    # 40. 
    # 41. 
    # 4
