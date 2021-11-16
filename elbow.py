# k inertia is a 2D array, col 1 = tested ks, col 2
def find_elbow(k_inertia):
    # exclude the first point because it is largest
    k_inertia_changes = np.array([1, None])

    for i in range(1, len(k_inertia)-2):
        iner_decrease_prior = k_inertia[i-1, 1] - k_inertia[i, 1]
        iner_decrease_post = k_inertia[i, 1] - k_inertia[i+1, 1]
        percent_decrease = ((iner_decrease_post)/iner_decrease_prior)
        k_inertia_changes = np.vstack(
            (k_inertia_changes, [k_inertia[i, 0], percent_decrease]))

    # exclude the first point, which is None
    ind = np.argmin(k_inertia_changes[1:, 1])+1
    best_k = int(k_inertia[ind, 0])

    return best_k, ind, k_inertia_changes


def find_elbow_plot(k_inertia):
    best_k_ind = find_elbow(k_inertia)[1]

    plt.plot(list(range(1, len(k_inertia)+1)),
             k_inertia[:, 1], "-ok", label="Inertia")
    plt.title("**Elbow Plot** \n Inertia = SSR from Respective Centroids")
    plt.ylabel("Inertia")
    plt.xlabel("k-value")

    # elbow
    plt.plot(k_inertia[best_k_ind, 0], k_inertia[best_k_ind, 1],
             "or", ms=8, label="Elbow (Automatically Found)")
    plt.legend()
