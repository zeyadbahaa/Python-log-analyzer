def analyze_log(filename):
    error_count = 0
    warning_count = 0
    info_count = 0
    unknown = 0

    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1
            else:
                unknown += 1

    return info_count, warning_count, error_count, unknown


info_count, warning_count, error_count, unknown = analyze_log("app.log")

print("============== LOG ANALYSIS ============")
print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
print(f"ERROR: {error_count}")