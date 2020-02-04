# python3

import requests, os, sys, time, datetime, ctypes

if __name__ == "__main__":
	# CONFIGURATIONS
	config_filename = "config.txt"
	config = { line.split('=')[0]: line.split('=')[1] for line in open(config_filename).read().split('\n') if len(line) != 0 }

	url = "https://poe.trade/search"
	league = config["league"]
	seller = config["target_account"]
	
	# http post poe trade
	post_json_offline = {"league":league,"type":"","base":"","name":"","dmg_min":"","dmg_max":"","aps_min":"","aps_max":"","crit_min":"","crit_max":"","dps_min":"","dps_max":"","edps_min":"","edps_max":"","pdps_min":"","pdps_max":"","armour_min":"","armour_max":"","evasion_min":"","evasion_max":"","shield_min":"","shield_max":"","block_min":"","block_max":"","sockets_min":"","sockets_max":"","link_min":"","link_max":"","sockets_r":"","sockets_g":"","sockets_b":"","sockets_w":"","linked_r":"","linked_g":"","linked_b":"","linked_w":"","rlevel_min":"","rlevel_max":"","rstr_min":"","rstr_max":"","rdex_min":"","rdex_max":"","rint_min":"","rint_max":"","mod_name":"","mod_min":"","mod_max":"","mod_weight":"","group_type":"And","group_min":"","group_max":"","group_count":"1","q_min":"","q_max":"","level_min":"","level_max":"","ilvl_min":"","ilvl_max":"","rarity":"","progress_min":"","progress_max":"","sockets_a_min":"","sockets_a_max":"","map_series":"","altart":"","identified":"","corrupted":"","crafted":"","enchanted":"","fractured":"","synthesised":"","mirrored":"","veiled":"","shaper":"","elder":"","crusader":"","redeemer":"","hunter":"","warlord":"","seller":seller,"thread":"","online":"","capquality":"x","buyout_min":"","buyout_max":"","buyout_currency":"","has_buyout":"","exact_currency":""}

	post_json_online = {"league":league,"type":"","base":"","name":"","dmg_min":"","dmg_max":"","aps_min":"","aps_max":"","crit_min":"","crit_max":"","dps_min":"","dps_max":"","edps_min":"","edps_max":"","pdps_min":"","pdps_max":"","armour_min":"","armour_max":"","evasion_min":"","evasion_max":"","shield_min":"","shield_max":"","block_min":"","block_max":"","sockets_min":"","sockets_max":"","link_min":"","link_max":"","sockets_r":"","sockets_g":"","sockets_b":"","sockets_w":"","linked_r":"","linked_g":"","linked_b":"","linked_w":"","rlevel_min":"","rlevel_max":"","rstr_min":"","rstr_max":"","rdex_min":"","rdex_max":"","rint_min":"","rint_max":"","mod_name":"","mod_min":"","mod_max":"","mod_weight":"","group_type":"And","group_min":"","group_max":"","group_count":"1","q_min":"","q_max":"","level_min":"","level_max":"","ilvl_min":"","ilvl_max":"","rarity":"","progress_min":"","progress_max":"","sockets_a_min":"","sockets_a_max":"","map_series":"","altart":"","identified":"","corrupted":"","crafted":"","enchanted":"","fractured":"","synthesised":"","mirrored":"","veiled":"","shaper":"","elder":"","crusader":"","redeemer":"","hunter":"","warlord":"","seller":seller,"thread":"","online":"x","capquality":"x","buyout_min":"","buyout_max":"","buyout_currency":"","has_buyout":"","exact_currency":""}

	r = requests.post(url, data=post_json_offline)
	search = r.text.find("Nothing was found. Try widening your search criteria.")
	
	if search != -1:
		print("{} has no items to sell! Cannot tell if online or not...".format(seller))

	else:
		r = requests.post(url, data=post_json_online)
		search = r.text.find("Nothing was found. Try widening your search criteria.")

		if search != -1:
			print("{} is offline!".format(seller))
		else:
			print("{} is online!".format(seller))