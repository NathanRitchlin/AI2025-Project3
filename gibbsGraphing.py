import math
import matplotlib.pyplot as plt
def sumDiff(actual, reported):
    totalDiff = 0
    for i in range(len(actual)):
        diff = actual[i] - reported[i]
        diff = math.fabs(diff)
        totalDiff += diff
    return totalDiff/2


#Calculating difference on child network, no evidence (gibbs sampling)
actual = [.05, 0.33, 0.29, 0.23, 0.05, 0.05]
reported = [0.044355, 0.335015, 0.29129, 0.226205, 0.05964, 0.043495]
totalDiff1 = sumDiff(actual,reported)

#child network, little evidence
actual = [.14, 0.18, 0.22, 0.17, 0.07, 0.23]
reported = [0.130035, 0.12738, 0.23335, 0.17213, 0.060015, 0.27709]
totalDiff2 = sumDiff(actual,reported)

#child network, moderate evidence
actual = [0.03, 0.07, 0.52, 0.30, 0.02, 0.05]
reported = [0.04721, 0.12297, 0.66827, 0.056955, 0.03644, 0.068155]
totalDiff3 = sumDiff(actual,reported)
print(totalDiff1, totalDiff2, totalDiff3)



values = [round(totalDiff1, 6), round(totalDiff2, 6), round(totalDiff3, 6)]
labels = ['None', 'Little', 'Moderate']

plt.figure()
bars = plt.bar(labels, values)
plt.ylim(0, 1)
plt.xlabel("Amount of Evidence")
plt.ylabel("Distribution Difference")
plt.title(" ")
for bar, value in zip(bars, values):
    plt.text(
        bar.get_x() + bar.get_width()/2,  # center x-position
        value + 0.02,                     # a little above the bar
        f"{value}",                       # text to display
        ha='center',                      # horizontal alignment
        va='bottom'                       # vertical alignment
    )
plt.savefig("GibbsChildNetwork1.png")

#Insurance network no evidence
actual =[[ 0.93, 0.03, 0.02, 0.02], [0.97, 0.02, 0.01, 0.01], [0.56, 0.32, 0.11,
0.02]]
reported = [[0.957055, 0.01995, 0.01388, 0.009115], [0.983445, 0.009855, 0.004115, 0.002585], [0.622365, 0.33109, 0.040775, 0.00577]]
totalDiff1 = 0
for i in range(len(reported)):
    totalDiff1 += sumDiff(actual[i], reported[i])

totalDiff1/= 3

actual =[[0.82, 0.08, 0.06, 0.04], [0.92, 0.04, 0.02, 0.02], [0.34, 0.35, 0.27, 0.04]]
reported = [[0.773405, 0.10317, 0.07193, 0.051495], [0.90327, 0.046045, 0.03004, 0.020645], [0.274685, 0.324085, 0.347885, 0.053345]]
totalDiff2 = 0
for i in range(len(reported)):
    totalDiff2 += sumDiff(actual[i], reported[i])

totalDiff2/= 3

actual =[[0.96, 0.02, 0.01, 0.01], [0.95, 0.03, 0.02, 0.01], [0.45, 0.22, 0.29, 0.05]]
reported = [[0.976765, 0.01353, 0.00464, 0.005065], [0.97003, 0.01612, 0.009105, 0.004745], [0.55107, 0.273235, 0.15317, 0.022525]]
totalDiff3 = 0
for i in range(len(reported)):
    totalDiff3 += sumDiff(actual[i], reported[i])

totalDiff3/= 3
print(totalDiff1, totalDiff2, totalDiff3)

values = [round(totalDiff1, 6), round(totalDiff2, 6), round(totalDiff3, 6)]
labels = ['None', 'Little', 'Moderate']

plt.figure()
bars = plt.bar(labels, values)
plt.ylim(0, 1)  # Scale y-axis from 0 to 1
plt.xlabel("Amount of Evidence")
plt.ylabel("Average Distribution Difference")
plt.title(" ")
for bar, value in zip(bars, values):
    plt.text(
        bar.get_x() + bar.get_width()/2,  # center x-position
        value + 0.02,                     # a little above the bar
        f"{value}",                       # text to display
        ha='center',                      # horizontal alignment
        va='bottom'                       # vertical alignment
    )
plt.savefig("GibbsInsuranceNetwork1.png")

actual = [(0.57, 0.43), (0.95, 0.05), (0.11, 0.89), (0.09, 0.91), (0.14, 0.86),
(0.88, 0.12)]
reported = [[0.3123455, 0.6876545], [0.822083, 0.177917], [0.1461065, 0.8538935], [0.2014715, 0.7985285], [0.22544, 0.77456], [0.7091565, 0.2908435]]
totalDiff1 = 0
for i in range(len(reported)):
    totalDiff1 += sumDiff(actual[i], reported[i])
totalDiff1/= 6
print(totalDiff1)

actual = [(0.92, 0.08), (0.13, 0.87), (0.11, 0.89),
(0.15, 0.85), (0.81 ,0.19)]
reported = [[1.0, 0.0], [0.0068785, 0.9931215], [0.0212285, 0.9787715], [0.0408555, 0.9591445], [0.8908905, 0.1091095]]
totalDiff2 = 0
for i in range(len(reported)):
    totalDiff2 += sumDiff(actual[i], reported[i])
totalDiff2/= 5
print(totalDiff2)



actual = [(0.35, 0.65), (0.51, 0.49), (0.54, 0.46),
(0.39, 0.61), (0.40, 0.60)]
reported = [[0.1977315, 0.8022685], [0.520383, 0.479617], [0.5600265, 0.4399735], [0.4080305, 0.5919695], [0.3576855, 0.6423145]]
totalDiff3 = 0
for i in range(len(reported)):
    totalDiff3 += sumDiff(actual[i], reported[i])
totalDiff3/= 5
print(totalDiff3)

actual = [(0.49, 0.51), (0.76, 0.24), (0.26, 0.74), (0.24,
0.76), (0.67, 0.33)]
reported = [[0.520208, 0.479792], [0.9728815, 0.0271185], [0.050114, 0.949886], [0.0630785, 0.9369215], [0.944053, 0.055947]]
totalDiff4 = 0
for i in range(len(reported)):
    totalDiff4 += sumDiff(actual[i], reported[i])
totalDiff4/= 5
print(totalDiff4)

actual = [(0.46, 0.54), (0.67, 0.33), (0.34, 0.66), (0.28,
0.72), (0.63, 0.37)]
reported = [[0.504992, 0.495008], [0.6326365, 0.3673635], [0.34019, 0.65981], [0.194707, 0.805293], [0.6598105, 0.3401895]]
totalDiff5 = 0
for i in range(len(reported)):
    totalDiff5 += sumDiff(actual[i], reported[i])
totalDiff5/= 5
print(totalDiff5)

actual = [(0.53, 0.47), (0.85, 0.15), (0.19, 0.81), (0.18, 0.82), (0.79, 0.21)]
reported = [[0.4401375, 0.5598625], [1.0, 0.0], [0.007507, 0.992493], [0.0500555, 0.9499445], [0.891934, 0.108066]]
totalDiff6 = 0
for i in range(len(reported)):
    totalDiff6 += sumDiff(actual[i], reported[i])
totalDiff6/= 5
print(totalDiff6)

actual = [(0.29, 0.71), (0.73, 0.27), (0.31, 0.69), (0.28, 0.72), (0.24, 0.76)]
reported = [[0.332654, 0.667346], [0.941195, 0.058805], [0.0440365, 0.9559635], [0.0574985, 0.9425015], [0.630043, 0.369957]]
totalDiff7 = 0
for i in range(len(reported)):
    totalDiff7 += sumDiff(actual[i], reported[i])
totalDiff7/= 5
print(totalDiff7)

values = [round(totalDiff1, 6), round(totalDiff2, 6), round(totalDiff3, 6), round(totalDiff4, 6), round(totalDiff5, 6), round(totalDiff6, 6), round(totalDiff7, 6)]
labels = ['None', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6']

plt.figure()
bars = plt.bar(labels, values)
plt.ylim(0, 1)  # Scale y-axis from 0 to 1
plt.xlabel("Problem Evidence Given")
plt.ylabel("Average Distribution Difference")
plt.title(" ")
for bar, value in zip(bars, values):
    plt.text(
        bar.get_x() + bar.get_width()/2,  # center x-position
        value + 0.02,                     # a little above the bar
        f"{value}",                       # text to display
        ha='center',                      # horizontal alignment
        va='bottom'                       # vertical alignment
    )
plt.savefig("GibbsWin95Network1.png")