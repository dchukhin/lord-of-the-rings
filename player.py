#!/usr/bin/python

from items.items import Items

#TODO: Get startingInventory from GameLoader instead
from items.starting_inventory import startingInventory

import constants

class Player(object):
    """
    Represents the (human) player.
    """
    
    def __init__(self, name, location):
        """
        Initializes the player.
        
        @param name:             The name of the player (e.g. "Frodo").
        @param location:         The location of player.
        """
        self._name = name
        self._location = location
        self._inventory = Items(startingInventory)

        self._level = constants.STARTING_LEVEL
        self._experience = constants.STARTING_EXPERIENCE

        #TODO: May want to use the levelUp() method to calculate this
        #(even though it may seem silly to 'level up' to the first level,
        # the levelUp method should really be responsible for
        # maintaining formulas for attack, hp, etc.
        self._attack = self._level * constants.attackStat
        self._hp = self._level * constants.hpStat

    def attack(self, target):
        """
        Allows player to attack target.

        @param target:     The target player is to attack.
        """
        target.takeDamage(self._attack)

        #TODO: Probably want to have BattleEngine be responsible for
        #reporting battle events -JDL
        print "%s attacked %s for %s damage!" %(self._name, target, self._attack)

    def takeDamage(self, damage):
        """
        Allows player to receive damage.

        @param damage):    The damage player is to receive.
        """
        self._hp -= damage
        print "%s took %s damage!" %(self._name, self._attack)

    def levelUp(self):
        """
        Levels up player and updates player stats. 
        """
        #TODO: Write levelUp() method
        pass

    def updateLocation(self, newLocation):
        #TODO: Consider replacing this with moveNorth(), moveSouth(), etc.
        #      methods. (Or, create a move() method that takes a direction
        #      (which should be defined in constants). -JDL

        self._location = newLocation

    def getLocation(self):
        """
        Returns player's current location (i.e. space).

        @return:    Player's current location.
        """
        return self._location
