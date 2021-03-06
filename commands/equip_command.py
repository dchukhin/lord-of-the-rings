#!/usr/bin/python

from command import Command

class EquipCommand(Command):
    """
    Equips player with item in inventory.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new equip command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Equips player with item in inventory.
        """
        itemToEquip = raw_input("Which item do you want to equip? \n")
        
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        
        itemInventory = inventory.getItemByName(itemToEquip)
        itemEquipment = equipped.getItemByName(itemToEquip)
        
        #Checks if item is in inventory and is not already equipped
        print ""
        if not itemInventory:
            print "%s is not in your inventory!" % itemToEquip
            return
        
        if itemEquipment:
            print "%s is already equipped!" % itemToEquip
            return

        #Equips player with item
        self._player.equip(itemInventory)
