team join nocollision @e[team=!nocollision,type=#christmas:passive_mobs]

execute as @a[scores={adorn_hot_chocolate_use=1..}] run function christmas:drink_hot_chocolate
execute as @a[scores={adorn_nether_wart_coffee_use=1..}] run function christmas:drink_coffee
execute as @a[scores={adorn_glow_berry_tea_use=1..}] run function christmas:drink_glow_berry_tea

execute at @e[type=snowyspirit:sled] run fill ~2 ~2 ~2 ~-2 ~-2 ~-2 minecraft:snow replace minecraft:snow
execute at @e[type=snowyspirit:sled] run fill ~1 ~1 ~3 ~-1 ~-1 ~-3 minecraft:snow replace minecraft:snow
execute at @e[type=snowyspirit:sled] run fill ~3 ~1 ~1 ~-3 ~-1 ~-1 minecraft:snow replace minecraft:snow

execute as @e[type=minecraft:armor_stand, tag=!armed] run function christmas:arm_armor_stand
execute as @e[type=minecraft:zombie, tag=!doorstopped] run function christmas:zombie_doorstop
