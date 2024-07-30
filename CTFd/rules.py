from flask import Blueprint, render_template

from CTFd.constants.config import  Configs
from CTFd.utils.dates import ctf_ended, ctf_paused, ctf_started
from CTFd.utils.decorators import (
    during_ctf_time_only,
    require_complete_profile
)
from CTFd.utils.helpers import get_errors, get_infos

rules = Blueprint("rules", __name__)


@rules.route("/rules")
@require_complete_profile
@during_ctf_time_only
def listing():

    infos = get_infos()
    errors = get_errors()

    if ctf_started() is False:
        errors.append(f"{Configs.ctf_name} has not started yet")

    if ctf_paused() is True:
        infos.append(f"{Configs.ctf_name} is paused")

    if ctf_ended() is True:
        infos.append(f"{Configs.ctf_name} has ended")

    return render_template("rules.html", infos=infos, errors=errors)
