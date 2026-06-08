log_file = "sample_log.txt"
failed_logins = 0

with open(log_file, "r") as file:
	for line in file:
		if "Failed login attempt" in line:
			failed_logins += 1

print(f"Total failed login attempts: {failed_logins}")

if failed_logins >= 5:
	print("ALERT: Suspicious login activity detected!")

else:
	print("No suspicious activity detected.")
