from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Xử lý đăng nhập
        return redirect(url_for("main.index"))
    return render_template("login.html")
