import os, sys, subprocess

# check if target dir specified
if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
	target_dir = sys.argv[1]
	for frmt in (".mp4",".webm"):
		for target_video in [x for x in os.listdir(target_dir) if frmt == x[-4:]]:
			subprocess.run(["python3", "main.py", "-i", f"{target_dir}/{target_video}", "-z", "3"], shell=False)
		if len(sys.argv) >= 3 and sys.argv[2] in ("rm","-rm"):
			os.system(f"rm -rf {target_dir}/*{frmt}")
	os.system(f"notify-send \"ezgif-essentials\" \"Finished creating .gif from {target_dir}\" --urgency=critical")
else:
	print("No target directory specificed or target directory specified is not valid directory/does not exist.")

