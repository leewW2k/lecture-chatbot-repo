import Image from "next/image";
import Link from "next/link";
import { Poppins } from "next/font/google";

import { cn } from "@/lib/utils";

const font = Poppins({
  subsets: ["latin"],
  weight: ["200", "300", "400", "500", "600", "700", "800"],
});

export function Logo() {
  return (
    <Link href="/">
      <div className="flex items-center gap-x-4 hover:opacity-75 transition">
        <div className="bg-white rounded-full p-1 mr-12 shrink-0 lg:mr-0 lg:shrink">
          <Image src="/spooky.svg" alt="GameHub" height="32" width="32" />
        </div>
        <div className={cn(font.className, "hidden lg:block")}>
          <p className="text-xl font-semibold">Lecture Companion</p>
          <p className="text-sm text-muted-foreground">Let&apos;s Learn Together</p>
        </div>
      </div>
    </Link>
  );
}