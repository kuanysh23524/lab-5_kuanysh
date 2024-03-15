import random

# Network traffic modeling
def generate_network_traffic():
    traffic_types = ['normal', 'suspicious', 'highly suspicious']
    return random.choice(traffic_types)

# Detection of suspicious activity
def detect_intrusion(traffic):
    if traffic == 'suspicious':
        return "Suspicious activity detected!"
    elif traffic == 'highly suspicious':
        return "Highly suspicious activity detected!"
    else:
        return "No suspicious activity was detected."

# Output of results
def report_intrusion(intrusion_detected):
    print(intrusion_detected)


def main():
    for i in range(10):
        traffic = generate_network_traffic()
        intrusion = detect_intrusion(traffic)
        report_intrusion(intrusion)

main()
