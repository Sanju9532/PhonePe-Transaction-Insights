url_get = "https://github.com/PhonePe/pulse.git"
save_to = "C:\phonepay-project"
from git import Repo

Repo.clone_from(url_get,save_to)
