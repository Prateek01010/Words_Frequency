import matplotlib.pyplot as plt
import string

# Given blog text
blog_text = """
The U.S. government on Wednesday said the Chinese state-sponsored hacking group known as Volt Typhoon had been embedded into some critical infrastructure networks in the country for at least five years.

Targets of the threat actor include communications, energy, transportation, and water and wastewater systems sectors in the U.S. and Guam.

"Volt Typhoon's choice of targets and pattern of behavior is not consistent with traditional cyber espionage or intelligence gathering operations, and the U.S. authoring agencies assess with high confidence that Volt Typhoon actors are pre-positioning themselves on IT networks to enable lateral movement to OT assets to disrupt functions," the U.S. government said.

The idea is to pre-position themselves on IT networks by maintaining persistence and understanding the target environment over time for disruptive or destructive cyber attacks against U.S. critical infrastructure in the event of a major crisis or conflict with the country.

The joint advisory, which was released by the Cybersecurity and Infrastructure Security Agency (CISA), National Security Agency (NSA), and the Federal Bureau of Investigation (FBI), was also backed by other nations that are part of the Five Eyes (FVEY) intelligence alliance comprising Australia, Canada, New Zealand, the U.K.

Volt Typhoon – which is also called Bronze Silhouette, Insidious Taurus, UNC3236, Vanguard Panda, or Voltzite – a stealthy China-based cyber espionage group that's believed to be active since June 2021.

It first came to light in May 2023 when FVEY and Microsoft revealed that the hacking crew managed to establish a persistent foothold into critical infrastructure organizations in the U.S. and Guam for extended periods of time sans getting detected by principally leveraging living-off-the-land (LotL) techniques.

"This kind of tradecraft, known as 'living off the land,' allows attackers to operate discreetly, with malicious activity blending in with legitimate system and network behavior making it difficult to differentiate – even by organizations with more mature security postures," the U.K. National Cyber Security Centre (NCSC) said.

Another hallmark tactic adopted by Volt Typhoon is the use of multi-hop proxies like KV-botnet to route malicious traffic through a network of compromised routers and firewalls in the U.S. to mask its true origins.

Cybersecurity firm CrowdStrike, in a report published in June 2023, called out its reliance on an extensive arsenal of open-source tooling against a narrow set of victims to achieve its strategic goals.

"Volt Typhoon actors conduct extensive pre-exploitation reconnaissance to learn about the target organization and its environment; tailor their tactics, techniques, and procedures (TTPs) to the victim's environment; and dedicate ongoing resources to maintaining persistence and understanding the target environment over time, even after initial compromise," the agencies noted.

"The group also relies on valid accounts and leverages strong operational security, which combined, allows for long-term undiscovered persistence."

Furthermore, the nation-state has been observed attempting to obtain administrator credentials within the network by exploiting privilege escalation flaws, subsequently leveraging the elevated access to facilitate lateral movement, reconnaissance, and full domain compromise.

The ultimate goal of the campaign is to retain access to the compromised environments, "methodically" re-targeting them over years to validate and expand their unauthorized accesses. This meticulous approach, per the agencies, is evidenced in cases where they have repeatedly exfiltrated domain credentials to ensure access to current and valid accounts.

"In addition to leveraging stolen account credentials, the actors use LOTL techniques and avoid leaving malware artifacts on systems that would cause alerts," CISA, FBI, and NSA said.

"Their strong focus on stealth and operational security allows them to maintain long-term, undiscovered persistence. Further, Volt Typhoon's operational security is enhanced by targeted log deletion to conceal their actions within the compromised environment."

The development comes as the Citizen Lab revealed a network of at least 123 websites impersonating local news outlets spanning 30 countries in Europe, Asia, and Latin America that's pushing pro-China content in a widespread influence campaign linked to a Beijing public relations firm named Shenzhen Haimaiyunxiang Media Co., Ltd.

The Toronto-based digital watchdog, which dubbed the influence operation PAPERWALL, said it shares similarities with HaiEnergy, albeit with different operators and unique TTPs.

"A central feature of PAPERWALL, observed across the network of websites, is the ephemeral nature of its most aggressive components, whereby articles attacking Beijing's critics are routinely removed from these websites some time after they are published," the Citizen Lab said.

In a statement shared with Reuters, a spokesperson for China's embassy in Washington said "it is a typical bias and double standard to allege that the pro-China contents and reports are 'disinformation,' and to call the anti-China ones 'true information.'"
"""

# Function to count the frequency of each alphabet
def count_alphabet_frequency(text):
    alphabet_frequency = {char: 0 for char in string.ascii_uppercase}
    
    for char in text:
        if char.isalpha():
            char = char.upper()
            alphabet_frequency[char] += 1
    
    return alphabet_frequency

# Counting alphabet frequency
frequency_dict = count_alphabet_frequency(blog_text)

# Calculating total characters for percentage calculation
total_characters = sum(frequency_dict.values())

# Calculating percentage and creating a bar chart
labels = list(frequency_dict.keys())
percentages = [(count / total_characters) * 100 for count in frequency_dict.values()]

# Creating a bar chart with percentage values above bars
fig, ax = plt.subplots()
bars = ax.bar(labels, percentages)

# Displaying percentage values above each bar
for bar, percentage in zip(bars, percentages):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{percentage:.2f}%', ha='center', va='bottom')

plt.xlabel('Alphabet')
plt.title('Alphabet Frequency in Blog')
plt.show()
