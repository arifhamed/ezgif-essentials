import os, sys, subprocess

if len(sys.argv) >= 2:
	target_dir = sys.argv[1]
	for target_video in [x for x in os.listdir(target_dir) if ".mp4" == x[-4:]]:
		subprocess.run(["python3", "main.py", "-i", f"{target_dir}/{target_video}", "-z", "3"], shell=False)
	os.system(f"notify-send \"ezgif-essentials\" \"Finished creating .gif from {target_dir}\" --urgency=critical")
else:
	print("No target directory specificed.")

